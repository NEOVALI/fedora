Name:           tela-icon-theme
Version:        20220828
Release:        2%{?dist}
Summary:        A flat colorful design icon theme
License:        GPLv3
URL:            https://github.com/vinceliuice/Tela-icon-theme
Source0:        %{url}/archive/refs/tags/2022-08-28.tar.gz
BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  bc
BuildRequires:	autoconf automake gtk3-devel
Requires:       gnome-themes-extra 

%description
A flat colorful design icon theme

%prep
%setup -c
%define _iconsdir %{_datadir}/icons/


%build
# Nothing to build


%install
install -d %{buildroot}%{_iconsdir}
cd Tela-icon-theme-2022-08-28
./install.sh -a -d %{buildroot}%{_iconsdir}


%files
%dir %{_iconsdir}
%{_iconsdir}/Tela*


%changelog

