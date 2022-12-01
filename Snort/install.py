import subprocess

library = 'apt install -y gcc libpcre3-dev zlib1g-dev libluajit-5.1-dev libpcap-dev openssl libssl-dev libnghttp2-dev ' \
          'libdumbnet-dev bison flex libdnet autoconf libtool'

subprocess.run(library)
