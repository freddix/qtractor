Summary:	Audio/MIDI multi-track sequencer
Name:		qtractor
Version:	0.5.5
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/qtractor/%{name}-%{version}.tar.gz
# Source0-md5:	ec3ad0f427a9e629fb0c42d10b4c2259
Patch0:		%{name}-desktop.patch
URL:		http://qtractor.sourceforge.net/
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	dssi
BuildRequires:	gtk+-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel
BuildRequires:	liblilv-devel
BuildRequires:	libmad-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libsuil-devel
BuildRequires:	libvorbis-devel
BuildRequires:	qt-linguist
BuildRequires:	qt-qmake
BuildRequires:	rubberband-devel
BuildRequires:	vst-plugins-sdk
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
# for lv2 plugins
Requires:	libsuil-gui-support
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio/MIDI multi-track sequencer.

%prep
%setup -q
%patch0 -p1

# use comman qt locale location
sed -i "s|@localedir@|%{_datadir}/qt/translations|" Makefile.in

%build
%{__autoheader}
%{__autoconf}
%configure \
	--disable-slv2	\
	--enable-lilv	\
	--enable-suil	\
	--with-vst=%{_includedir}/vst
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --without-mo --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png

