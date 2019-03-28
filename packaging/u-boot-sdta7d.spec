Name: u-boot-sdta7d
Summary: Bootloader for Sdta7d boards based on ARM processor
Version: 2019.01
Release: 0
Group: System/Kernel
License: GPL-2.0+
ExclusiveArch: %{arm}
URL: http://www.denx.de/wiki/U-Boot
Source0: %{name}-%{version}.tar.bz2

BuildRequires: bison
BuildRequires: flex

%description
bootloader for SDTA7D Embedded boards based on ARM processor

%prep
%setup -q

%build

# Set configuration
make sdta7d_defconfig

# Build image
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

# u-boot sdta7d installation
mkdir -p %{buildroot}/boot/u-boot
install -d %{buildroot}/boot/u-boot
install -m 755 ./SPL %{buildroot}/boot/u-boot
install -m 755 ./u-boot.img %{buildroot}/boot/u-boot

%clean

%files
%defattr(-,root,root,-)
/boot/u-boot/SPL
/boot/u-boot/u-boot.img

