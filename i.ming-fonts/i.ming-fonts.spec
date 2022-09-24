Name:           i.ming-fonts
Version:        8.00
Release:        1%{?dist}
Summary:        I.明體（I.Ming）乃係一套依照傳承字形標準化文件《傳承字形部件檢校表》的推薦字形標準，並以TrueType格式封裝、依照Unicode編碼的OpenType字型。
License:        IPA-1.0
Url:            https://github.com/ichitenfont/I.Ming
Source0:        https://raw.githubusercontent.com/ichitenfont/I.Ming/master/LICENSE.md
Source1:        %{url}/raw/master/%{version}/I.Ming-%{version}.ttf
Source2:        %{url}/raw/master/%{version}/I.MingCP-%{version}.ttf
Source3:        %{url}/raw/master/%{version}/I.MingVar-%{version}.ttf
Source4:        %{url}/raw/master/%{version}/I.MingVarCP-%{version}.ttf
Source5:        %{url}/raw/master/%{version}/PMingI.U-%{version}.ttf
Source6:        %{url}/raw/master/%{version}/PMingI.UVar-%{version}.ttf
BuildRequires:  fontpackages-devel
BuildArch:      noarch

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
I.明體（I.Ming）乃係一套依照傳承字形標準化文件《傳承字形部件檢校表》的推薦字形標準，並以TrueType格式封裝、依照Unicode編碼的OpenType字型。

%prep
%define _ttfontsdir /usr/share/fonts/i.ming

%build
cp %{S:0} ./LICENSE

%install
install -d %{buildroot}%{_ttfontsdir}
install -m 644 %{S:1} %{buildroot}%{_ttfontsdir}
install -m 644 %{S:2} %{buildroot}%{_ttfontsdir}
install -m 644 %{S:3} %{buildroot}%{_ttfontsdir}
install -m 644 %{S:4} %{buildroot}%{_ttfontsdir}
install -m 644 %{S:5} %{buildroot}%{_ttfontsdir}
install -m 644 %{S:6} %{buildroot}%{_ttfontsdir}

%post
%postun

%files
%license LICENSE
%{_ttfontsdir}/*.ttf
%dir %{_ttfontsdir}

%changelog

