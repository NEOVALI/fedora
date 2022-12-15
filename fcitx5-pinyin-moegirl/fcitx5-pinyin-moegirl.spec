Name:           fcitx5-pinyin-moegirl
Version:        20221214
Release:        1%{?dist}
Summary:        Fcitx 5 pinyin dictionary generator for MediaWiki instances. (Releases for demo dict of zh.moegirl.org.cn)
License:        Unlicense;CC-BY-NC-SA-3.0
Url:            https://github.com/outloudvi/mw2fcitx
Source0:        https://github.com/outloudvi/mw2fcitx/releases/download/%{version}/moegirl.dict
Source1:        https://raw.githubusercontent.com/outloudvi/mw2fcitx/master/LICENSE
BuildArch:      noarch

Requires:       fcitx5
Requires:       fcitx5-chinese-addons

%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%description
Fcitx 5 pinyin dictionary generator for MediaWiki instances. (Releases for demo dict of zh.moegirl.org.cn)

%prep
%define BUILD_DIR %{_builddir}/%{name}-%{version}

%build
cp %{_sourcedir}/LICENSE %{_builddir}/LICENSE

%install
install -Dm644 %{SOURCE0} -t %{buildroot}%{_datadir}/fcitx5/pinyin/dictionaries/

%post
%postun

%files
%license LICENSE
%{_datadir}/fcitx5/pinyin/dictionaries/moegirl.dict

%changelog
