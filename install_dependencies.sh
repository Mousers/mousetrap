#!/bin/bash
# Run this script to install the dependencies for Mousetrap on Fedora 21.
# Must give a target path as an argument to download OpenCV to.


if [ -n "$1" ]; then
	targetdir=$1
else
	echo "No target path for OpenCV specified"
	exit 1
fi


sudo yum -y install cmake python3 python3-devel python3-numpy gcc gcc-c++ python3-PyYAML.x86_64 gnome-common python3-setuptools
sudo pip3 install numpy
sudo rpm -ivh http://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo/fedora-21-x86_64/python3-xlib-0.15git20141113-1.fc21/python3-xlib-0.15git20141113-1.fc21.noarch.rpm

cd $targetdir
git clone --branch 3.0.0-alpha --depth 1 https://github.com/Itseez/opencv.git
cd opencv
git checkout 3.0.0-alpha

mkdir release
cd release

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") -D PYTHON_EXECUTABLE=$(which python3) ..
make -j4
sudo make install


