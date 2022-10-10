%define debug_package %{nil}
%define _build_id_links none


Name:           yesplaymusic
Version:        0.4.5
Release:        1%{?dist}
Summary:        A client for QQ and more.


License:        AGPL v3
URL:            https://github.com/qier222/YesPlayMusic
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/raw/master/build/icons/512x512.png
Source2:        https://github.com/valig5/fedora/raw/main/yesplaymusic/yesplaymusic.desktop
Source3:        %{url}/raw/master/LICENSE


BuildRequires:  bash
BuildRequires:  tar
BuildRequires:  gtk3


Requires:       gtk3
Requires:       libappindicator-gtk3


%description
%{summary}


%prep
%autosetup -n yesplaymusic-%{version}
cp %{S:3} ./


%build
# nothing to build


%install
install -d %{buildroot}/opt/yesplaymusic
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_datadir}/applications/

cp -r * %{buildroot}/opt/yesplaymusic
cp -r %{S:1} %{buildroot}/opt/yesplaymusic/yesplaymusic.png
install -Dm644 %{S:2} %{buildroot}/%{_datadir}/applications/yesplaymusic.desktop


%post
ln -s /opt/yesplaymusic/yesplaymusic %{_bindir}/yesplaymusic


%postun
rm -f %{_bindir}/yesplaymusic


%files
%license LICENSE
%dir /opt/yesplaymusic
/opt/yesplaymusic/*
%{_datadir}/applications/yesplaymusic.desktop


%changelog

