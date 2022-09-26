Name:           clash-verge
Version:        1.1.0
Release:        1%{?dist}
Summary:        A Clash GUI based on tauri.
License:        MIT
Url:            https://github.com/zzzgydi/clash-verge
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/valig5/fedora/raw/main/clash-verge/clash-verge.desktop

BuildRequires:  nodejs
BuildRequires:  npm
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
BuildRequires:  rust-openssl+default-devel
BuildRequires:  webkit2gtk3
BuildRequires:  libappindicator-gtk3 
BuildRequires:  yarnpkg

Requires:       webkit2gtk3
Requires:       libappindicator-gtk3 

BuildArch:      x86_64

%description
A Clash GUI based on tauri.


%define debug_package %{nil}


%prep
%setup -n %{name}-%{version}
cp %{S:1} ./


%build
# build
yarn install
yarn run check
yarn build


%install

# install bin
install -d %{buildroot}/%{_bindir}
install -Dm755 ./src-tauri/target/release/%{name} -t %{buildroot}/%{_bindir} # clash-verge
install -Dm755 ./src-tauri/target/release/clash -t %{buildroot}/%{_bindir} # clash
install -Dm755 ./src-tauri/target/release/clash-meta -t %{buildroot}/%{_bindir} # clash-meta

# buildroot/usr/lib/resources
install -d %{buildroot}/%{_libdir}/%{name}/resources 
install -Dm644 ./src-tauri/resources/Country.mmdb -t %{buildroot}/%{_libdir}/%{name}/resources

# icons
install -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps 
install -Dm644 ./src/assets/image/logo.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg 

# 桌面图标
install -d %{buildroot}/%{_datadir}/applications 
install -Dm644 ./%{name}.desktop -t %{buildroot}/%{_datadir}/applications


%post
%postun


%files
%{_bindir}/%{name}
%{_bindir}/clash
%{_bindir}/clash-meta
%dir %{_libdir}/%{name}/resources
%{_libdir}/%{name}/resources/Country.mmdb
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog

