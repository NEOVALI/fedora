%global         source_name Bibata_Cursor
%global         debug_package %{nil}

Name:           bibata-cursor-themes
Version:        1.1.2
Release:        1%{?dist}
Summary:        OpenSource, Compact and Material Designed Cursor Se
License:        GNU General Public License v3.0
URL:            https://github.com/ful1e5/Bibata_Cursor
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/bitmaps.zip

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
%__mkdir -p bitmaps
%__unzip %{SOURCE1} -d bitmaps

%build
pip install clickgen

cd builder
%__make build_unix

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
