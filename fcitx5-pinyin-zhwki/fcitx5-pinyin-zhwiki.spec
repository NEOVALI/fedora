%define         _webslangver        20221128
%define         _converterver       0.2.4

Name:           fcitx5-pinyin-zhwiki
Version:        %{_converterver}.%{_webslangver}
Release:        1%{?dist}
Summary:        Fcitx 5 Pinyin Dictionary from zh.wikipedia.org
License:        GFDL
Url:            https://github.com/felixonmars/fcitx5-pinyin-zhwiki
Source0:        https://github.com/felixonmars/fcitx5-pinyin-zhwiki/releases/download/%{_converterver}/zhwiki-%{_webslangver}.dict
Source1:        https://raw.githubusercontent.com/felixonmars/fcitx5-pinyin-zhwiki/master/LICENSE
BuildArch:      noarch

Requires:       fcitx5
Requires:       fcitx5-chinese-addons

%description
%{summary} .

%prep
%define BUILD_DIR %{_builddir}/%{name}-%{version}

%build
cp %{_sourcedir}/LICENSE %{_builddir}/LICENSE

%install
install -Dm644 %{SOURCE0} %{buildroot}%{_datadir}/fcitx5/pinyin/dictionaries/zhwiki.dict

%files
%license LICENSE
%{_datadir}/fcitx5/pinyin/dictionaries/zhwiki.dict

%changelog
