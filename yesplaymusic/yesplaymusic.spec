Name:           yesplaymusic
Version:        0.4.5
Release:        1%{?dist}
Summary:        High appearance third-party Netease Cloud Music
License:        MIT
Url:            https://github.com/qier222/YesPlayMusic
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/raw/master/image/logo.png
Source2:        https://github.com/valig5/fedora/raw/main/%{name}/%{name}.desktop

BuildRequires:  tar
Requires:       libappindicator-gtk3 

BuildArch:      x86_64

%undefine _missing_build_ids_terminate_build
%global debug_package %{nil}

%description
High appearance third-party Netease Cloud Music.


%prep
%setup -c

%build

%install
install -d %{buildroot}/opt/%{name}
cp -r ./%{name}-%{version}/* %{buildroot}/opt/%{name}/
install -d %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps
install -Dm644 %{S:1} %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
install -d %{buildroot}/%{_datadir}/applications
install -Dm644 %{S:2} -t %{buildroot}/%{_datadir}/applications


%post
ln -sf '/opt/%{name}/yesplaymusic' '/usr/bin/yesplaymusic'
chmod 4755 '/opt/%{name}/chrome-sandbox' || true
update-mime-database /usr/share/mime || true
update-desktop-database /usr/share/applications || true

%postun
rm -f '/usr/bin/yesplaymusic'

%files
%dir /opt/%{name}
/opt/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

%changelog