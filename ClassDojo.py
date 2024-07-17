#!/usr/bin/env python3

"""
Download all ClassDojo photos and videos in your timeline.
by kecebongsoft
How it works:
1. Fetch list of items in the timeline, if there are multiple pages,
   it will fetch for all pages.
2. Collect list of URLs for the attachment for each item.
3. Download the files into a local temporary directory, and also save
   the timeline activity as a JSON file.
How to use:
1. Modify the session cookie in this script, check your session cookie
   by opening ClassDojo in a browser and copy the following cookies:
   dojo_log_session_id, dojo_login.sid, and dojo_home_login.sid.
2. Run this script and wait for it to finish.
If errors happen:
1. Ensure your path is correct if you are on Linux.
2. Make sure "classdojo_output" directory exists in the same folder as this script.
3. Make sure you have the correct session cookies set in this script.
4. Make sure you can open the FEED_URL listed in this script from within your browser (assuming you can open the ClassDojo website).
"""

import requests
import json
import os
import tempfile

FEED_URL = 'https://home.classdojo.com/api/storyFeed?includePrivate=true'
DESTINATION = tempfile.mkdtemp(dir='classdojo_output')  # Ensure this directory exists in the same place as this script.

SESSION_COOKIES = {
    'dojo_log_session_id': 'copy here',
    'dojo_login.sid': 'copy here',
    'dojo_home_login.sid': 'copy here',
}

NOT_BEFORE = '0000-00-00'  # '2020-08-22'

def get_items(feed_url):
    print('Fetching items: %s ...' % feed_url)
    resp = requests.get(feed_url, cookies=SESSION_COOKIES)
    data = resp.json()
    prev = data.get('_links', {}).get('prev', {}).get('href')
    
    print(f"Fetched {len(data['_items'])} items.")
    return data['_items'], prev

def get_contents(feed_url):
    items, prev = get_items(feed_url)

    while prev and feed_url != prev:
        prev_urls, prev = get_items(prev)
        items.extend(prev_urls)
    
    # Save the JSON data for later/inspection.
    with open(os.path.join(DESTINATION, 'data.json'), 'w') as fd:
        fd.write(json.dumps(items, indent=4))
    
    contents = []
    total = 0
    for item in items:
        data = item['contents']
        entry = {
            'description': data.get('body'),
            'base_name': None,
            'day': None,
            'attachments': [],
        }
        attachments = data.get('attachments', {})
        if not attachments:
            continue

        for attachment in attachments:
            parts = attachment['path'].split('/')
            day = parts[-3]
            if parts[3] == 'api' or day < NOT_BEFORE:
                continue
            total += 1
            if not entry['base_name']:
                entry['base_name'] = parts[-4]
                entry['day'] = day
            entry['attachments'].append({'name': '_'.join(parts[-2:]),
                                         'url': attachment['path']})

        if entry['base_name']:
            contents.append(entry)

    return contents, total

def download_contents(contents, total):
    index = 0
    highest_day = contents[0]['day']
    for entry in contents:
        description_name = '{}_{}_description.txt'.format(entry['day'], entry['base_name'])
        with open(os.path.join(DESTINATION, description_name), 'wt') as fd:
            fd.write(entry['description'])
        for item in entry['attachments']:
            index += 1
            day = entry['day']
            if day > highest_day:
                highest_day = day
            url = item['url']
            filename = os.path.join(DESTINATION, '{}_{}_{}'.format(entry['day'], entry['base_name'], item['name']))
            if os.path.exists(filename):
                continue
            print('Downloading {}/{} on {}: {}'.format(index, total, day, item['name']))
            try:
                with open(filename, 'wb') as fd:
                    resp = requests.get(url, cookies=SESSION_COOKIES)
                    if resp.status_code == 200:
                        fd.write(resp.content)
                        print(f"Successfully downloaded: {filename}")
                    else:
                        print(f"Failed to download {filename}. Status code: {resp.status_code}")
            except Exception as e:
                print(f"Error downloading {filename}: {e}")
    print('Last day of data download: {}'.format(highest_day))
    print('Done!')

if __name__ == '__main__':
    print('Starting')
    if not os.path.exists(DESTINATION):
        os.makedirs(DESTINATION)
    contents, total = get_contents(FEED_URL)
    download_contents(contents, total)
