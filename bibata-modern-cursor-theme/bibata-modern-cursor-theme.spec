Name:           bibata-modern-cursor-theme
Version:        1.1.2
Release:        1%{?dist}
Summary:        OpenSource, Compact and Material Designed Cursor Set
License:        GNU General Public License v3.0
URL:            https://github.com/ful1e5/Bibata_Cursor
Source0:        %{url}/releases/download/v%{version}/Bibata-Modern.tar.gz
Source1:        %{url}/raw/main/LICENSE
Source2:        %{url}/raw/main/README.md

BuildArch:      noarch

Requires:       gtk3

%description
OpenSource, Compact and Material Designed Cursor Set

%prep
%autosetup -c -n %{name}-%{version}
cp %{S:1} ./
cp %{S:2} ./
%define _iconsdir /usr/share/icons/

%build

%install
install -d %{buildroot}%{_iconsdir}
cp -r ./Bibata-* %{buildroot}%{_iconsdir}

%post
%postun

%files
%license LICENSE
%doc README.md
%{_iconsdir}/Bibata*

%changelog