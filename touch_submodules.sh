# Initialize a new .gitmodules file
touch .gitmodules

# Add each submodule and checkout the specific commit

# DeepLSD
git submodule add https://github.com/cvg/DeepLSD.git third-party/DeepLSD
cd third-party/DeepLSD
git checkout 59006b2
cd ../../

# GlueStick
git submodule add https://github.com/cvg/GlueStick.git third-party/GlueStick
cd third-party/GlueStick
git checkout 40d71d5
cd ../../

# Hierarchical-Localization
git submodule add https://github.com/cvg/Hierarchical-Localization.git third-party/Hierarchical-Localization
cd third-party/Hierarchical-Localization
git checkout 61e0cd0
cd ../../

# HighFive
git submodule add https://github.com/B1ueber2y/HighFive.git third-party/HighFive
cd third-party/HighFive
git checkout 5e77ac3
cd ../../

# JLinkage
git submodule add https://github.com/B1ueber2y/JLinkage.git third-party/JLinkage
cd third-party/JLinkage
git checkout 3787a84
cd ../../

# RansacLib
git submodule add https://github.com/B1ueber2y/RansacLib.git third-party/RansacLib
cd third-party/RansacLib
git checkout 3bfa537
cd ../../

# TP-LSD
git submodule add https://github.com/rpautrat/TP-LSD.git third-party/TP-LSD
cd third-party/TP-LSD
git checkout 5558050
cd ../../

# hawp
git submodule add https://github.com/cherubicXN/hawp.git third-party/hawp
cd third-party/hawp
git checkout 45bd43f
cd ../../

# libigl
git submodule add https://github.com/B1ueber2y/libigl.git third-party/libigl
cd third-party/libigl
git checkout e19a68c
cd ../../

# pybind11
git submodule add https://github.com/pybind/pybind11.git third-party/pybind11
cd third-party/pybind11
git checkout b3a43d1
cd ../../

# pytlbd
git submodule add https://github.com/iago-suarez/pytlbd.git third-party/pytlbd
cd third-party/pytlbd
git checkout b0c8cfc
cd ../../

# pytlsd
git submodule add https://github.com/iago-suarez/pytlsd.git third-party/pytlsd
cd third-party/pytlsd
git checkout 21381ca
cd ../../

# Commit the Changes
git add .gitmodules third-party/
git commit -m "Update submodules to specific commits"
git push

