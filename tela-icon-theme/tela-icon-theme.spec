Name:           tela-icon-theme
Version:        2022.08.28
Release:        1%{?dist}
Summary:        A flat colorful design icon theme
License:        GPLv3
URL:            https://github.com/vinceliuice/Tela-icon-theme
Source0:        %{url}/archive/refs/tags/2022-08-28.tar.gz
BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  bc
Requires:       gnome-themes-extra

%description
A flat colorful design icon theme


%prep
%setup -q -n tela-icon-theme


%build
# Nothing to build

%install
THEME_DIRS="Tela
Tela-black
Tela-black-dark
Tela-blue
Tela-blue-dark
Tela-brown
Tela-brown-dark
Tela-dark
Tela-green
Tela-green-dark
Tela-grey
Tela-grey-dark
Tela-manjaro
Tela-manjaro-dark
Tela-nord
Tela-nord-dark
Tela-orange
Tela-orange-dark
Tela-pink
Tela-pink-dark
Tela-purple
Tela-purple-dark
Tela-red
Tela-red-dark
Tela-ubuntu
Tela-ubuntu-dark
Tela-yellow
Tela-yellow-dark"
%{__install} -d -m755 %{buildroot}%{_datadir}/icons/
# for file in Tela Tela-black Tela-black-dark Tela-blue Tela-blue-dark Tela-brown Tela-brown-dark Tela-dark Tela-green Tela-green-dark Tela-grey Tela-grey-dark Tela-manjaro Tela-manjaro-dark Tela-nord Tela-nord-dark Tela-orange Tela-orange-dark Tela-pink Tela-pink-dark Tela-purple Tela-purple-dark Tela-red Tela-red-dark Tela-ubuntu Tela-ubuntu-dark Tela-yellow Tela-yellow-dark ; do
for file in ${THEME_DIRS}
do
  %{__cp} -pr ${file} %{buildroot}%{_datadir}/icons/
done


%files
%defattr(-,root,root)
%{_datadir}/icons/Tela
%{_datadir}/icons/Tela-black
%{_datadir}/icons/Tela-black-dark
%{_datadir}/icons/Tela-blue
%{_datadir}/icons/Tela-blue-dark
%{_datadir}/icons/Tela-brown
%{_datadir}/icons/Tela-brown-dark
%{_datadir}/icons/Tela-dark
%{_datadir}/icons/Tela-green
%{_datadir}/icons/Tela-green-dark
%{_datadir}/icons/Tela-grey
%{_datadir}/icons/Tela-grey-dark
%{_datadir}/icons/Tela-manjaro
%{_datadir}/icons/Tela-manjaro-dark
%{_datadir}/icons/Tela-nord
%{_datadir}/icons/Tela-nord-dark
%{_datadir}/icons/Tela-orange
%{_datadir}/icons/Tela-orange-dark
%{_datadir}/icons/Tela-pink
%{_datadir}/icons/Tela-pink-dark
%{_datadir}/icons/Tela-purple
%{_datadir}/icons/Tela-purple-dark
%{_datadir}/icons/Tela-red
%{_datadir}/icons/Tela-red-dark
%{_datadir}/icons/Tela-ubuntu
%{_datadir}/icons/Tela-ubuntu-dark
%{_datadir}/icons/Tela-yellow
%{_datadir}/icons/Tela-yellow-dark


%changelog
* Sun Sep 25 2022 five <156211398@qq.com> - 2022-08-28
- update to 2022-08-28