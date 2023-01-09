%global debug_package %{nil}

Name:           clash-verge
Version:        1.2.1
Release:        2%{?dist}
Summary:        A Clash GUI based on tauri.
License:        MIT
Url:            https://github.com/zzzgydi/clash-verge
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/NEOVALI/fedora/raw/main/clash-verge/clash-verge.desktop

BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  jq
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  wget
BuildRequires:  webkit2gtk4.0-devel
BuildRequires:  rust-gobject-sys+default-devel
BuildRequires:  rust-pango+default-devel
BuildRequires:  rust-cairo-rs+default-devel 
BuildRequires:  rust-atk-sys+default-devel
BuildRequires:  rust-gdk-sys+default-devel
BuildRequires:  moreutils
BuildRequires:  rust-openssl+default-devel
BuildRequires:  webkit2gtk4.0
BuildRequires:  libappindicator-gtk3 
BuildRequires:  yarnpkg
BuildRequires:  clash-meta-bin
BuildRequires:  clash-premium-bin


Requires:       webkit2gtk4.0
Requires:       libappindicator-gtk3 
Requires:       clash-meta-bin
Requires:       clash-premium-bin
Requires:       clash-geoip

BuildArch:      x86_64

%description
A Clash GUI based on tauri.



%prep
%setup -n %{name}-%{version}
install -d ./src-tauri/sidecar
ln -sf /usr/bin/clash ./src-tauri/sidecar/clash-x86_64-unknown-linux-gnu
ln -sf /usr/bin/clash-meta ./src-tauri/sidecar/clash-meta-x86_64-unknown-linux-gnu


cd src-tauri
# only build the excutable
jq '.tauri.bundle.active = false' tauri.conf.json|sponge tauri.conf.json
# disable updater
jq '.tauri.updater.active = false' tauri.conf.json|sponge tauri.conf.json
cd ..

%build
# build
export RUSTFLAGS="-L /usr/lib/quickjs"
yarn install
yarn run check
yarn build


%install
install -d %{buildroot}/usr/lib/%{name}/resources/
# bin
install -d %{buildroot}/%{_bindir}
install -Dm755 ./src-tauri/target/release/%{name} -t %{buildroot}/%{_bindir} # clash-verge

# icons
install -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps 
install -Dm644 ./src/assets/image/logo.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg 

# .deskop
install -d %{buildroot}/%{_datadir}/applications 
install -Dm644 %{S:1} -t %{buildroot}/%{_datadir}/applications


%post
ln -sf /etc/clash/Country.mmdb /usr/lib/%{name}/resources/Country.mmdb
%postun
rm -rf /usr/lib/%{name}/resources/Country.mmdb

%files
%license LICENSE
%{_bindir}/%{name}
%dir /usr/lib/%{name}
%dir /usr/lib/%{name}/resources
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
