Name:           clash-verge
Version:        1.0.6
Release:        1%{?dist}
Summary:        A Clash GUI based on tauri.
License:        MIT
Url:            https://github.com/zzzgydi/clash-verge
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/valig5/fedora/raw/main/clash-verge/clash-verge.desktop

BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  yarnpkg
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  wget
BuildRequires:  webkit2gtk3-devel
BuildRequires:  rust-gobject-sys+default-devel
BuildRequires:  rust-pango+default-devel
BuildRequires:  rust-cairo-rs+default-devel 
BuildRequires:  rust-atk-sys+default-devel
BuildRequires:  rust-gdk-sys+default-devel
BuildRequires:  moreutils

Requires:       webkit2gtk3
Requires:       libappindicator-gtk3 
Requires:       libindicator-gtk3 
Requires:       libdbusmenu
Requires:       libdbusmenu-gtk3


%description
A Clash GUI based on tauri.

%prep
%setup -c -n %{name}-%{version}
%define BUILD_DIR %{_builddir}/%{name}-%{version}/

%build
cd %{BUILD_DIR}
# build
yarn install
yarn run check
yarn build

%install

install -Dm755 src-tauri/target/release/%{name} -t %{buildroot}/usr/bin
install -Dm755 src-tauri/target/release/clash -t %{buildroot}/usr/bin
install -Dm755 src-tauri/target/release/clash-meta -t %{buildroot}/usr/bin
install -d %{buildroot}/usr/lib/%{name}
install -d %{buildroot}/usr/lib/%{name}/resources
install -Dm644 src-tauri/resources/Country.mmdb -t %{buildroot}/usr/lib/%{name}/resources
install -Dm644 src/assets/image/logo.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/%{name}.svg
install -Dm644 %{S:1} -t %{buildroot}/usr/share/applications


%post
%postun

%files
/usr/bin/%{name}
/usr/bin/clash
/usr/bin/clash-meta
%dir /usr/lib/%{name}/resources
/usr/lib/%{name}/resources/Country.mmdb
/usr/share/applications/%{name}.desktop
/usr/share/icons/hicolor/scalable/apps/%{name}.svg


%changelog

