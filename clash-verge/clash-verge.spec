Name:           clash-verge
Version:        1.0.6
Release:        1%{?dist}
Summary:        A Clash GUI based on tauri.
License:        MIT
Url:            https://github.com/zzzgydi/clash-verge
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        motrix-launcher.sh
Source2:        motrix.desktop
Source3:        motrix.xml
BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  yarnpkg
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  webkit2gtk3-devel
BuildRequires:  wget

Requires:       webkit2gtk3 

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages
%define _build_id_links none

%description
A Clash GUI based on tauri.

%prep
%setup -q -n %{name}-%{version} -a 0
%define BUILD_DIR %{_builddir}/%{name}-%{version}/

%build
cd %{BUILD_DIR}
# real build
yarn install
yarn run check
yarn build

%install
mkdir -p "%{buildroot}/usr/bin"
cd "%{BUILD_DIR}"
install -Dm644 release/linux-unpacked/resources/app.asar -t "%{buildroot}/usr/lib/motrix/"
cp -r release/linux-unpacked/resources/engine "%{buildroot}/usr/lib/motrix/"
install -Dm644 static/512x512.png "%{buildroot}/usr/share/icons/hicolor/512x512/apps/motrix.png"
install -Dm755 %{SOURCE1} "%{buildroot}/usr/bin/motrix"
install -Dm644 %{SOURCE2} "%{buildroot}/usr/share/applications/motrix.desktop"
install -Dm644 %{SOURCE3} "%{buildroot}/usr/share/mime/packages/motrix.xml"

%post
%postun

%files
%{_bindir}/motrix
/usr/lib/motrix
/usr/share/applications/motrix.desktop
/usr/share/icons/hicolor/512x512/apps/motrix.png
/usr/share/mime/packages/motrix.xml

%changelog

