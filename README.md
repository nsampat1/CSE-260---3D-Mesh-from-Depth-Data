# CSE-260---3D-Mesh-from-Depth-Data
Code from https://github.com/mantoone/DepthCapture; Changed to capture one frame, Added printing of intrinsic matrix, intrinsic matrix dimensions, extrinsic matrix and pixel buffer height and width
uncompress.sh inside depthto3d.py contains the command: printf "\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x00" |cat - /tmp/Depth |gzip -dc >/tmp/bin_out.dat
