Name:           icalingua
Version:        2.7.7
Release:        1%{?dist}
Summary:        A client for QQ and more.
License:        GPL v3
Url:            https://github.com/Icalingua-plus-plus/Icalingua-plus-plus
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/raw/develop/art-src/xmas.png
Source2:        https://github.com/valig5/fedora/raw/main/%{name}/%{name}.desktop
BuildRequires:  tar
BuildArch:      x86_64

%undefine _missing_build_ids_terminate_build
%global debug_package %{nil}

%description
A client for QQ and more.


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
ln -sf '/opt/%{name}/icalingua' '/usr/bin/icalingua'
chmod 4755 '/opt/%{name}/chrome-sandbox' || true
update-mime-database /usr/share/mime || true
update-desktop-database /usr/share/applications || true

%postun
rm -f '/usr/bin/icalingua'

%files
%dir /opt/%{name}
/opt/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

%changelog