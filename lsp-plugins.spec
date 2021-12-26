#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : lsp-plugins
Version  : 1.1.31
Release  : 230
URL      : file:///aot/build/clearlinux/packages/lsp-plugins/lsp-plugins-v1.1.31.tar.gz
Source0  : file:///aot/build/clearlinux/packages/lsp-plugins/lsp-plugins-v1.1.31.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : PyYAML
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : alsa-lib-dev
BuildRequires : alsa-lib-dev32
BuildRequires : autogen
BuildRequires : autogen-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : buildreq-distutils3
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : cairo
BuildRequires : cairo-dev
BuildRequires : clr-rpm-config
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : dejagnu
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : expat-dev
BuildRequires : expat-staticdev
BuildRequires : expect
BuildRequires : fftw-dev
BuildRequires : fftw-staticdev
BuildRequires : findutils
BuildRequires : flac
BuildRequires : flac-dev
BuildRequires : flac-dev32
BuildRequires : flac-staticdev
BuildRequires : flac-staticdev32
BuildRequires : flex
BuildRequires : fluidsynth
BuildRequires : fluidsynth-dev
BuildRequires : fluidsynth-staticdev
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-go
BuildRequires : gcc-go-lib
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb-dev
BuildRequires : git
BuildRequires : glib
BuildRequires : glib-dev
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-doc
BuildRequires : glibc-extras
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : glibc-nscd
BuildRequires : glibc-staticdev
BuildRequires : glibc-utils
BuildRequires : gmp-dev
BuildRequires : googletest-dev
BuildRequires : graphviz
BuildRequires : gtk+-dev
BuildRequires : gtk3
BuildRequires : gtk3-dev
BuildRequires : guile
BuildRequires : ladspa_sdk
BuildRequires : ladspa_sdk-dev
BuildRequires : ladspa_sdk-staticdev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libjpeg-turbo
BuildRequires : libjpeg-turbo-dev
BuildRequires : libjpeg-turbo-staticdev
BuildRequires : liblo
BuildRequires : liblo-dev
BuildRequires : liblo-staticdev
BuildRequires : libogg-dev
BuildRequires : libogg-dev32
BuildRequires : libogg-staticdev
BuildRequires : libogg-staticdev32
BuildRequires : libpng-dev
BuildRequires : libpng-staticdev
BuildRequires : libsamplerate-dev
BuildRequires : libsamplerate-staticdev
BuildRequires : libsndfile-dev
BuildRequires : libsndfile-staticdev
BuildRequires : libstdc++
BuildRequires : libtool-dev
BuildRequires : libunwind-dev
BuildRequires : libvorbis-dev
BuildRequires : libvorbis-dev32
BuildRequires : libvorbis-staticdev
BuildRequires : libvorbis-staticdev32
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt
BuildRequires : lv2
BuildRequires : lv2-dev
BuildRequires : mesa
BuildRequires : mesa-dev
BuildRequires : meson
BuildRequires : mpc-dev
BuildRequires : mpfr-dev
BuildRequires : ncurses
BuildRequires : ncurses-dev
BuildRequires : ninja
BuildRequires : octave-dev
BuildRequires : opus
BuildRequires : opus-dev
BuildRequires : opus-lib
BuildRequires : opus-staticdev
BuildRequires : pcre-dev
BuildRequires : pcre-staticdev
BuildRequires : pcre2-dev
BuildRequires : pcre2-staticdev
BuildRequires : php
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(fftw3f)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(lv2)
BuildRequires : pkgconfig(rubberband)
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : procps-ng
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : rdflib
BuildRequires : sed
BuildRequires : serd
BuildRequires : serd-dev
BuildRequires : serd-staticdev
BuildRequires : sord
BuildRequires : sord-dev
BuildRequires : sord-staticdev
BuildRequires : speex-dev
BuildRequires : speex-staticdev
BuildRequires : speexdsp-dev
BuildRequires : speexdsp-staticdev
BuildRequires : sqlite-autoconf-dev
BuildRequires : sratom
BuildRequires : sratom-dev
BuildRequires : sratom-staticdev
BuildRequires : tcl
BuildRequires : texinfo
BuildRequires : util-linux
BuildRequires : valgrind-dev
BuildRequires : vamp-sdk
BuildRequires : vamp-sdk-dev
BuildRequires : vamp-sdk-staticdev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : zita-convolver
BuildRequires : zita-convolver-dev
BuildRequires : zita-convolver-staticdev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
==== ABOUT ====
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2 and LinuxVST formats.

%prep
%setup -q -n lsp-plugins-clr
cd %{_builddir}/lsp-plugins-clr

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640543551
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
## altflags1
unset ASFLAGS
export CFLAGS="-ggdb3 -ggnu-pubnames -gz=zlib -Og -fexceptions -static-libstdc++ -static-libgcc -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wp,-D_REENTRANT -fuse-ld=bfd -fuse-linker-plugin -feliminate-unused-debug-types -Wl,-sort-common -Wno-error -pipe -ffat-lto-objects -fPIC"
export ASMFLAGS="-ggdb3 -ggnu-pubnames -gz=zlib -Og -fexceptions -static-libstdc++ -static-libgcc -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wp,-D_REENTRANT -fuse-ld=bfd -fuse-linker-plugin -feliminate-unused-debug-types -Wl,-sort-common -Wno-error -pipe -ffat-lto-objects -fPIC"
export CXXFLAGS="-ggdb3 -ggnu-pubnames -gz=zlib -Og -fexceptions -static-libstdc++ -static-libgcc -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wp,-D_REENTRANT -fuse-ld=bfd -fuse-linker-plugin -feliminate-unused-debug-types -Wl,-sort-common -Wno-error -pipe -ffat-lto-objects -fPIC"
export FCFLAGS="-ggdb3 -ggnu-pubnames -gz=zlib -Og -fexceptions -static-libstdc++ -static-libgcc -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wp,-D_REENTRANT -fuse-ld=bfd -fuse-linker-plugin -feliminate-unused-debug-types -Wl,-sort-common -Wno-error -pipe -ffat-lto-objects -fPIC"
export FFLAGS="-ggdb3 -ggnu-pubnames -gz=zlib -Og -fexceptions -static-libstdc++ -static-libgcc -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wp,-D_REENTRANT -fuse-ld=bfd -fuse-linker-plugin -feliminate-unused-debug-types -Wl,-sort-common -Wno-error -pipe -ffat-lto-objects -fPIC"
export LDFLAGS="-ggdb3 -ggnu-pubnames -gz=zlib -Og -fexceptions -static-libstdc++ -static-libgcc -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wp,-D_REENTRANT -fuse-ld=bfd -fuse-linker-plugin -feliminate-unused-debug-types -Wl,-sort-common -Wno-error -pipe -ffat-lto-objects -fPIC"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/gbm:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/gbm:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=1
## altflags1 end
make  %{?_smp_mflags}   PREFIX=/usr LIB_PATH="/usr/lib64" V=1 VERBOSE=1 V=1 VERBOSE=1


%install
export SOURCE_DATE_EPOCH=1640543551
rm -rf %{buildroot}
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
## altflags1
unset ASFLAGS
export CFLAGS="-ggdb3 -ggnu-pubnames -gz=zlib -Og -fexceptions -static-libstdc++ -static-libgcc -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wp,-D_REENTRANT -fuse-ld=bfd -fuse-linker-plugin -feliminate-unused-debug-types -Wl,-sort-common -Wno-error -pipe -ffat-lto-objects -fPIC"
export ASMFLAGS="-ggdb3 -ggnu-pubnames -gz=zlib -Og -fexceptions -static-libstdc++ -static-libgcc -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wp,-D_REENTRANT -fuse-ld=bfd -fuse-linker-plugin -feliminate-unused-debug-types -Wl,-sort-common -Wno-error -pipe -ffat-lto-objects -fPIC"
export CXXFLAGS="-ggdb3 -ggnu-pubnames -gz=zlib -Og -fexceptions -static-libstdc++ -static-libgcc -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wp,-D_REENTRANT -fuse-ld=bfd -fuse-linker-plugin -feliminate-unused-debug-types -Wl,-sort-common -Wno-error -pipe -ffat-lto-objects -fPIC"
export FCFLAGS="-ggdb3 -ggnu-pubnames -gz=zlib -Og -fexceptions -static-libstdc++ -static-libgcc -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wp,-D_REENTRANT -fuse-ld=bfd -fuse-linker-plugin -feliminate-unused-debug-types -Wl,-sort-common -Wno-error -pipe -ffat-lto-objects -fPIC"
export FFLAGS="-ggdb3 -ggnu-pubnames -gz=zlib -Og -fexceptions -static-libstdc++ -static-libgcc -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wp,-D_REENTRANT -fuse-ld=bfd -fuse-linker-plugin -feliminate-unused-debug-types -Wl,-sort-common -Wno-error -pipe -ffat-lto-objects -fPIC"
export LDFLAGS="-ggdb3 -ggnu-pubnames -gz=zlib -Og -fexceptions -static-libstdc++ -static-libgcc -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wp,-D_REENTRANT -fuse-ld=bfd -fuse-linker-plugin -feliminate-unused-debug-types -Wl,-sort-common -Wno-error -pipe -ffat-lto-objects -fPIC"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/gbm:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/gbm:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=1
## altflags1 end
%make_install -- PREFIX="/usr" LIB_PATH="/usr/lib64" V=1 VERBOSE=1 SHELL="/bin/bash -x"

%files
%defattr(-,root,root,-)
