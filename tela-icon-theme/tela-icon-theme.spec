Name:           tela-icon-theme
Version:        2022.08.28
Release:        1%{?dist}
Summary:        A flat colorful design icon theme
License:        GPLv3
URL:            https://github.com/vinceliuice/Tela-icon-theme
Source0:        %{url}/archive/refs/tags/2022-08-28.tar.gz
Source1:        %{url}/raw/master/COPYING
BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  bc
BuildRequires:	autoconf automake gtk3-devel

Requires:       gnome-themes-extra 

%description
A flat colorful design icon theme

%prep
%setup -cn %{name}-%{version}
cp %{S:1} ./LICENSE
%define _iconsdir /usr/share/icons/

%build
# Nothing to build

%install
install -d %{buildroot}%{_iconsdir}
cd %{name}-%{version}
./install.sh -a -d %{buildroot}%{_iconsdir}

%files
%dir %{_iconsdir}
%{_iconsdir}/Tela*

%changelog

