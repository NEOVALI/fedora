%global         source_name Bibata_Cursor
%global         debug_package %{nil}

Name:           bibata-cursor-themes
Version:        2.0.0
Release:        1%{?dist}
Summary:        OpenSource, Compact and Material Designed Cursor Set

License:        GNU General Public License v3.0
URL:            https://github.com/ful1e5/Bibata_Cursor
Source0:        %{url}/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  npm
BuildRequires:  yarnpkg
BuildRequires:  python3
BuildRequires:  python3-pip
BuildRequires:  python3-virtualenv
BuildRequires:  libX11-xcb
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libpng-devel
BuildRequires:  gtk3-devel
BuildRequires:  nss
BuildRequires:  mesa-libgbm
BuildRequires:  alsa-lib

Requires:       gtk3

%description
OpenSource, Compact and Material Designed Cursor Set

%prep
%autosetup -n %{source_name}-%{version}

%build
pip install clickgen
pip install attrs

yarn build

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/icons
for theme in $(ls %{_builddir}/%{source_name}-%{version}/themes); do
  %__mv %{_builddir}/%{source_name}-%{version}/themes/${theme} %{buildroot}%{_datadir}/icons
  %__chmod 0755 %{buildroot}%{_datadir}/icons/${theme}
done

%clean
%__rm -rf %{buildroot}

%files
%license LICENSE
%doc README.md
%{_datadir}/icons/*

%changelog
* Mon Oct  3 12:07:28 EDT 2022 Peter Wu
- New Release - v2.0.0

* Sun 05 Jun 2022 07:54:12 PM EDT Peter Wu
- Use bitmaps.zip to build

* Mon Jul 12 09:44:23 AM EDT 2021 Peter Wu
- New Release - v1.1.2

* Fri Mar 26 09:52:42 AM EDT 2021 Peter Wu
- New Release - v1.1.1

* Fri Feb 26 09:45:42 EST 2021 Peter Wu
- New Release - v1.1.0

* Tue Nov 17 09:42:13 EST 2020 Peter Wu <peterwu@hotmail.com>
- New Release - v1.0.3
