Name:           adw-gtk3-theme
Version:        3.7
Release:        1%{?dist}
Summary:        The theme from libadwaita ported to GTK-3
License:        GPLv2+
URL:            https://github.com/lassekongo83/adw-gtk3
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  sassc
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  ninja-build

BuildArch:      noarch

%description
The theme from libadwaita ported to GTK-3


%global debug_package %{nil}


%prep
%autosetup -c -n %{name}-%{version}


%build
cd adw-gtk3-3.7
%meson
%meson_build


%install
cd adw-gtk3-3.7
%meson_install

%post


%postun


%files
%dir %{_datadir}/themes/adw-gtk3
%dir %{_datadir}/themes/adw-gtk3-dark
%{_datadir}/themes/adw-gtk3/*
%{_datadir}/themes/adw-gtk3-dark/*

%changelog
* Sun Sep 25 2022 five <156211398@qq.com> - 3.7-1
- update to 3.7