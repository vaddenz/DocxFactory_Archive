#!/usr/bin/env bash

echo "[x] Installing DocxFactory ..."

if [ -d "/opt/DocxFactory" ]; then
	echo "[x] Uninstalling older versions ..."
	sudo rm -r /opt/DocxFactory/
fi


echo "[x] Extracting files to /opt/ folder..."
sudo tar -zxf ./DocxFactoryLinux64.tar.gz -C /opt


# Add the DocxFactory/lib/ folder to the list of library
# to search when a program is running.
sudo echo /opt/DocxFactory/lib/ > /etc/ld.so.conf.d/DocxFactory.conf
sudo chmod 666 /etc/ld.so.conf.d/DocxFactory.conf
sudo ldconfig


echo "[x] Installing the DocxFactory python3 module ..."
cp ./test_install.py /opt/DocxFactory/python/test_install.py
cd /opt/DocxFactory/python
python3 /opt/DocxFactory/python/setup.py install


echo "[x] Testing if installation succeed ..."
python3 ./test_install.py
