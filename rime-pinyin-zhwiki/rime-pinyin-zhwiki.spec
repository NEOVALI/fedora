%define         _webslangver        20220909
%define         _converterver       0.2.4

Name:           rime-pinyin-zhwiki
Version:        %{_converterver}.%{_webslangver}
Release:        1%{?dist}
Summary:        RIME Pinyin Dictionary from zh.wikipedia.org
License:        GFDL
Url:            https://github.com/felixonmars/fcitx5-pinyin-zhwiki
Source0:        https://github.com/felixonmars/fcitx5-pinyin-zhwiki/releases/download/%{_converterver}/zhwiki-%{_webslangver}.dict.yaml
Source1:        https://raw.githubusercontent.com/felixonmars/fcitx5-pinyin-zhwiki/master/LICENSE
BuildArch:      noarch

Recommends:     librime

%description
%{summary} .

%prep
%define BUILD_DIR %{_builddir}/%{name}-%{version}

%build
cp %{_sourcedir}/LICENSE %{_builddir}/LICENSE

%install
install -Dm644 %{SOURCE0} %{buildroot}%{_datadir}/rime-data/zhwiki.dict.yaml

%files
%license LICENSE
%{_datadir}/rime-data/zhwiki.dict.yaml

%changelog