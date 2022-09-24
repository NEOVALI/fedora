Name:           sarasa-gothic-fonts
Version:        0.37.4
Release:        1%{?dist}
Summary:        SARASA GOTHIC, a CJK programing font based on Iosevka, Inter and Source Han Sans
License:        OFL-1.1
Url:            https://github.com/be5invis/Sarasa-Gothic
Source0:        https://github.com/be5invis/Sarasa-Gothic/releases/download/v%{version}/sarasa-gothic-ttc-%{version}.7z
Source1:        https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/master/LICENSE
BuildRequires:  fontpackages-devel
BuildRequires:  p7zip
BuildArch:      noarch

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
SARASA GOTHIC, a CJK programming font based on Iosevka, Inter and Source Han Sans.

%prep
%setup -qcn %{name}-%{version}
cp %{S:1} ./
%define _ttfontsdir /usr/share/fonts/sarasa-gothic

%build

%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -m 644 *.ttc %{buildroot}%{_ttfontsdir}

%post
%postun

%files
%license LICENSE
%{_ttfontsdir}/*.ttc
%dir %{_ttfontsdir}

%changelog
* Fri Sep 23 2022 hey5v <156211398@qq.com> - 0.37.4-1
- Update to 0.37.4

* Tue Mar 22 2022 zhullyb <zhullyb@outlook.com> - 0.36.1-1
- new version

