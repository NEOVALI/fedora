Name:           bilibili
Version:        1.6.1
Release:        1%{?dist}
Summary:        哔哩哔哩官方客户端linux移植版。Bilibili official desktop client


License:        MIT
URL:            https://github.com/msojocs/bilibili-linux
Source0:        %{url}/releases/download/v%{version}-3/io.github.msojocs.bilibili_%{version}-3_amd64.deb

BuildRequires:  tar

Requires:       gtk3
Requires:       libappindicator-gtk3
Requires:       ffmpeg


%description
%{summary}


%define debug_package %{nil}

%prep
ar -vx %{S:0}
tar -xvf data.tar.xz


%build
# nothing to build


%install
install -d %{buildroot}/opt/apps/
install -d %{buildroot}/%{_datadir}/applications/
install -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/

cp -r ./opt/apps/io.github.msojocs.bilibili %{buildroot}/opt/apps/
install -Dm644 ./usr/share/applications/io.github.msojocs.bilibili.desktop %{buildroot}/%{_datadir}/applications/io.github.msojocs.bilibili.desktop 
install -Dm644 ./usr/share/icons/hicolor/scalable/apps/io.github.msojocs.bilibili.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/io.github.msojocs.bilibili.svg

%post


%postun


%files
%dir /opt/apps/io.github.msojocs.bilibili
/opt/apps/io.github.msojocs.bilibili/*
%{_datadir}/applications/io.github.msojocs.bilibili.desktop
%{_datadir}/icons/hicolor/scalable/apps/io.github.msojocs.bilibili.svg

%changelog

