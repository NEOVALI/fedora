Name:           icalingua-plus-plus
Version:        2.7.3
Release:        1%{?dist}
Summary:        A client for QQ and more.

License:        AGPL v3
URL:            https://github.com/Icalingua-plus-plus/Icalingua-plus-plus
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  openssl

Requires:       gtk3
Requires:       libappindicator-gtk3

%description
%{summary}

%prep
%autosetup -c -n %{name}-%{version}
%define _pnpm "node %{buildsubdir}/node_modules/pnpm/bin/pnpm.cjs"

%build
cd Icalingua-plus-plus-2.7.3
npm install pnpm
%{_pnpm} install
%{_pnpm} run build:dir



%install
install -d %{buildroot}/opt/icalingua
install -d %{buildroot}/%{_libdir}
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_datadir}/applications/
install -d %{buildroot}/%{_datadir}/icons/hicolors/512x512/apps

cp -a icalingua/build/linux-x86_64-unpacked/* %{buildroot}/opt/icalingua
install -Dm644 pkgres/512x512.png %{buildroot}/%{_datadir}/icons/hicolors/512x512/apps/icalingua.png
install -Dm644 pkgres/icalingua.desktop %{buildroot}/%{_datadir}/applications/icalingua.desktop
ln -s /opt/icalingua/icalingua %{buildroot}/%{_bindir}/icalingua

%files
%license LICENSE
%dir /opt/icalingua
/opt/icalingua/*
%{_datadir}/icons/hicolors/512x512/apps/icalingua.png
%{_datadir}/applications/icalingua.desktop
{_bindir}/icalingua

%changelog

