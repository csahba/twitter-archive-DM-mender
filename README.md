# twitter-archive-DM-mender
Script that repairs downloaded twitter archives, allowing full access to direct message history

Several json objects in the files direct-messages.js, direct-message-headers.js etc in twitter archives are (for me at least) split up and most of my DM history is inaccessible in the viewer. This script restores the objects to working order (also maintains chronological order) so you can use the provided twitter archive viewer in the zip. The viewer is a bit meh, and there's other online solutions but at least this way maintains your precious memories' privacy ^_^

To use, just run the script or the exe in the data folder of the extracted archive.
I made an exe for windows users but if you're on macos you'll have to install python to run the script, in which case you'll need to run it from the command line in the data directory wherever you extracted your archive.
