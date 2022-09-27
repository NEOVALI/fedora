Name:           rime-pinyin-moegirl
Version:        20220925
Release:        1%{?dist}
Summary:        RIME pinyin dictionary generator for MediaWiki instances. (Releases for demo dict of zh.moegirl.org.cn)
License:        Unlicense;CC-BY-NC-SA-3.0
Url:            https://github.com/outloudvi/mw2fcitx
Source0:        https://github.com/outloudvi/mw2fcitx/releases/download/%{version}/moegirl.dict.yaml
Source1:        https://raw.githubusercontent.com/outloudvi/mw2fcitx/master/LICENSE
BuildArch:      noarch

Recommends:     librime

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
Fcitx 5 pinyin dictionary generator for MediaWiki instances. (Releases for demo dict of zh.moegirl.org.cn)

%prep
%define BUILD_DIR %{_builddir}/%{name}-%{version}

%build
cp %{_sourcedir}/LICENSE %{_builddir}/LICENSE

%install
install -Dm644 %{SOURCE0} -t %{buildroot}%{_datadir}/rime-data/

%post
%postun

%files
%license LICENSE
%{_datadir}/rime-data/moegirl.dict.yaml

%changelog