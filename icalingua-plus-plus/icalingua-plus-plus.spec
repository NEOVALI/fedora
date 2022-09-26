Name:           icalingua-plus-plus
Version:        2.7.3
Release:        1%{?dist}
Summary:        A client for QQ and more.


License:        AGPL v3
URL:            https://github.com/Icalingua-plus-plus/Icalingua-plus-plus
Source0:        %{url}/releases/download/v%{version}/icalingua-%{version}.tar.xz
Source1:        %{url}/raw/development/pkgres/512x512.png
Source2:        https://github.com/valig5/fedora/raw/main/icalingua-plus-plus/icalingua.desktop
Source3:        %{url}/raw/development/LICENSE


BuildRequires:  bash
BuildRequires:  tar
BuildRequires:  gtk3


Requires:       gtk3
Requires:       libappindicator-gtk3


%description
%{summary}


%define debug_package %{nil}


%prep
%autosetup -n icalingua-%{version}
cp %{S:3} ./


%build
# nothing to build


%install
install -d %{buildroot}/opt/icalingua
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_datadir}/applications/
install -d %{buildroot}/%{_datadir}/icons/hicolors/512x512/apps

cp -r * %{buildroot}/opt/icalingua
install -Dm644 %{S:1} %{buildroot}/%{_datadir}/icons/hicolors/512x512/apps/icalingua.png
install -Dm644 %{S:2} %{buildroot}/%{_datadir}/applications/icalingua.desktop


%post
ln -s /opt/icalingua/icalingua %{_bindir}/icalingua


%postun
rm -f %{_bindir}/icalingua


%files
%license LICENSE
%dir /opt/icalingua
/opt/icalingua/*
%{_datadir}/icons/hicolors/512x512/apps/icalingua.png
%{_datadir}/applications/icalingua.desktop


%changelog
