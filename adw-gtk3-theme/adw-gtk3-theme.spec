Name:           adw-gtk3-theme
Version:        3.7
Release:        1%{?dist}
Summary:        The theme from libadwaita ported to GTK-3
License:        GPLv2+
URL:            https://github.com/lassekongo83/adw-gtk3
BuildRequires: sassc
BuildRequires: git
BuildRequires: meson
BuildRequires: ninja-build

%description
The theme from libadwaita ported to GTK-3

%prep
git clone --recurse-submodules https://github.com/lassekongo83/adw-gtk3.git

%build
cd adw-gtk3
git checkout tags/v%{version}
%meson
%meson_build

%install
cd adw-gtk3
%meson_install

%files
%{_datadir}/themes/adw-gtk3/*
%{_datadir}/themes/adw-gtk3-dark/*

%changelog
* Sun Sep 25 2022 five <156211398@qq.com> - 3.7-1
- update to 3.7