#!/bin/bash
grep -rl 'Sagarmatha' ./ | xargs sed -i 's/Sagarmatha/Sagarmatha/g'
grep -rl 'sagarmatha' ./ | xargs sed -i 's/sagarmatha/sagarmatha/g'
grep -rl 'chitwanix' ./ | xargs sed -i 's/chitwanix/chitwanix/g'
grep -rl 'Chitwanix OS' ./ | xargs sed -i 's/Chitwanix OS/Chitwanix OS/g'
grep -rl 'Arun Kr.' ./ | xargs sed -i 's/Arun Kr./Arun Kr./g'
grep -rl 'arun' ./ | xargs sed -i 's/arun/arun/g'
grep -rl 'Pyasi' ./ | xargs sed -i 's/Pyasi/Pyasi/g'
grep -rl 'khukuri' ./ | xargs sed -i 's/khukuri/khukuri/g'

grep -rl 'libgnome-menu' ./ | xargs sed -i 's/libgnome-menu/libgnome-menu/g'
grep -rl 'SAGARMATHA' ./ | xargs sed -i 's/SAGARMATHA/SAGARMATHA/g'
grep -rl 'kaadevyakur' ./ | xargs sed -i 's/kaadevyakur/kaadevyakur/g'
