#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v18
# autospec commit: eaa4f711da30
#
Name     : pypi-torchvision
Version  : 0.19.1
Release  : 1
URL      : https://github.com/pytorch/vision/archive/v0.19.1/vision-0.19.1.tar.gz
Source0  : https://github.com/pytorch/vision/archive/v0.19.1/vision-0.19.1.tar.gz
Summary  : image and video datasets and models for torch deep learning
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: pypi-torchvision-license = %{version}-%{release}
Requires: pypi-torchvision-python = %{version}-%{release}
Requires: pypi-torchvision-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(torch)
BuildRequires : pypi(wheel)
BuildRequires : pytorch-python3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
These files come from the GIFLIB project (https://giflib.sourceforge.net/) and
are licensed under the MIT license.

%package license
Summary: license components for the pypi-torchvision package.
Group: Default

%description license
license components for the pypi-torchvision package.


%package python
Summary: python components for the pypi-torchvision package.
Group: Default
Requires: pypi-torchvision-python3 = %{version}-%{release}

%description python
python components for the pypi-torchvision package.


%package python3
Summary: python3 components for the pypi-torchvision package.
Group: Default
Requires: python3-core
Provides: pypi(torchvision)
Requires: pypi(numpy)
Requires: pypi(pillow)
Requires: pypi(torch)

%description python3
python3 components for the pypi-torchvision package.


%prep
%setup -q -n vision-0.19.1
cd %{_builddir}/vision-0.19.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725902366
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-torchvision
cp %{_builddir}/vision-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-torchvision/f5caa6a036441a2f13cbd6ed856145777b28c00d || :
cp %{_builddir}/vision-%{version}/test/assets/damaged_jpeg/TensorFlow-LICENSE %{buildroot}/usr/share/package-licenses/pypi-torchvision/c8070154137bf553054d8e3c25b5fe4c4352ef44 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-torchvision/c8070154137bf553054d8e3c25b5fe4c4352ef44
/usr/share/package-licenses/pypi-torchvision/f5caa6a036441a2f13cbd6ed856145777b28c00d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
