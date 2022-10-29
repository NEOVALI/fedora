%global debug_package %{nil}

Name:           aliyun-drive-xiaobaiyang
Version:        2.9.24
Release:        1%{?dist}
Summary:        基于阿里云盘网页版开发的PC客户端，支持win7-11，macOS，linux
License:        MIT
Url:            https://github.com/liupan1890/aliyunpan
Source0:        %{url}/releases/download/v%{version}/Linux.v%{version}.zip
Source1:        https://github.com/valig5/fedora/raw/main/aliyun-drive-xiaobaiyang/aliyun-drive-xiaobaiyang.desktop
Source2:        https://github.com/valig5/fedora/raw/main/aliyun-drive-xiaobaiyang/app.asar

BuildRequires:  p7zip

Requires:       mpv
Requires:       libappindicator-gtk3
Requires:       aria2

BuildArch:      x86_64

%description
基于阿里云盘网页版开发的PC客户端，支持win7-11，macOS，linux

%prep
%setup -qcn %{name}-%{version}
mv * %{name}
cd %{name}
mv linux#U4f7f#U7528#U5e2e#U52a9.txt README.txt
mv \#U963f#U91cc#U4e91#U76d8#U5c0f#U767d#U7f8a#U7248 阿里云盘小白羊版

%build


%install
install -d %{buildroot}/opt
cp -r aliyun-drive-xiaobaiyang %{buildroot}/opt
cp -r %{S:2} %{buildroot}/opt/aliyun-drive-xiaobaiyang/electron/resources/

# .deskop
install -d %{buildroot}/%{_datadir}/applications
install -Dm644 %{S:1} -t %{buildroot}/%{_datadir}/applications


%post
ln -s /usr/bin/aria2c /opt/aliyun-drive-xiaobaiyang/electron/resources/aria2c

%postun


%files
%dir /opt/aliyun-drive-xiaobaiyang
/opt/aliyun-drive-xiaobaiyang/*
/%{_datadir}/applications/aliyun-drive-xiaobaiyang.desktop

%changelog
