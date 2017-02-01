#!/usr/bin/python

# Copyright KOLIBERO under one or more contributor license agreements.  
# KOLIBERO licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import argparse

def convert():
  map = {}
  with open(args.input, 'r') as myfile:
    data = myfile.read().replace('\n', '')
    srcarr = json.loads(data)
    for i in srcarr:
      #print i
      #ii = json.loads(i)
      map[i.get(args.key)] = i.get(args.value)
    #print map
    with open(args.output, 'w') as outfile:
      outfile.write(json.dumps(map))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="arr2map")
  parser.add_argument('--input', default="source.json")
  parser.add_argument('--output', default="target.json")
  parser.add_argument('--key', default="game_id")
  parser.add_argument('--value', default="id")

  args = parser.parse_args()
  print "source:",args.input
  print "target:",args.output
  print "key:",args.key
  print "value:",args.value

  convert()
