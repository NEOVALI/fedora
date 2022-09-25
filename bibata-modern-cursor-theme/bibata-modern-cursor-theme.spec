Name:           bibata-modern-cursor-themes
Version:        1.1.2
Release:        1%{?dist}
Summary:        OpenSource, Compact and Material Designed Cursor Set
License:        GNU General Public License v3.0
URL:            https://github.com/ful1e5/Bibata_Cursor
Source0:        %{url}/releases/download/v%{version}/Bibata-Modern.tar.gz

BuildArch:      noarch

Requires:       gtk3

%description
OpenSource, Compact and Material Designed Cursor Set

%prep
%autosetup -n %{name}-%{version}

%build

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/icons
for theme in $(ls %{_builddir}/%{name}-%{version}/themes); do
  %__mv %{_builddir}/%{name}-%{version}/themes/${theme} %{buildroot}%{_datadir}/icons
  %__chmod 0755 %{buildroot}%{_datadir}/icons/${theme}
done

%clean
%__rm -rf %{buildroot}

%files
%license LICENSE
%doc README.md
%{_datadir}/icons/*

%changelog
