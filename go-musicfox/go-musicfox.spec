Name:           go-musicfox
Version:        3.0.2
Release:        1%{?dist}
Summary:        Command-line Netease Cloud Music written in Go.
License:        MIT
Url:            https://github.com/anhoder/go-musicfox
Source0:        %{url}/releases/download/v%{version}/%{name}_%{version}_linux_amd64.zip
Source1:        %{url}/raw/master/LICENSE

BuildRequires:  p7zip
BuildArch:      x86_64



%description
Command-line Netease Cloud Music written in Go.

%define debug_package %{nil}


%prep
%autosetup -c

%build
cp %{S:1} ./LICENSE


%install
install -d %{buildroot}/%{_bindir}
install -Dm755 ./%{name}_%{version}_linux_amd64/musicfox %{buildroot}/%{_bindir}/musicfox


%post

%postun


%files
%license LICENSE
%{_bindir}/musicfox


%changelog
