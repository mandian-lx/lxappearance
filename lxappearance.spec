Summary:	A new feature-rich GTK+ theme switcher
Name:     	lxappearance
Version:	0.5.1
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://downloads.sourceforge.net/project/lxde/%name-%version.tar.gz
Patch0:		po.fuzzy.patch
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel desktop-file-utils
BuildRequires:	intltool
Suggests: lxappearance-obconf

%description
LXAppearance is a new GTK+ theme switcher developed for project LXDE.

%package devel
Group:		Graphical desktop/Other
Summary:	%{name} developement files
Provides:	%{name}-devel = %{version}-%{release}
Requires:	pkgconfig

%description devel
This package contains header files needed when building applications based on
%{name}.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

desktop-file-install --vendor="" \
	--remove-key="NotShowIn" \
	--add-only-show-in="LXDE" \
	--dir=%buildroot%_datadir/applications %buildroot%_datadir/applications/*.desktop


%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/%name
%{_mandir}/man1/lxappearance.*

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/lxappearance.pc


%changelog
* Wed Aug 03 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.1-2mdv2011.0
+ Revision: 692982
- update to 0.5.1

* Wed Jun 01 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.0-8
+ Revision: 682386
- add font hinting and render config with translate

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-7
+ Revision: 666109
- mass rebuild

* Sat Mar 19 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.0-6
+ Revision: 647041
- move unstable patch for fonts hinting and antialiasing in fork package

* Thu Feb 17 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.0-5
+ Revision: 638301
- add antialias and hinting settings

* Fri Dec 31 2010 Александр Казанцев <kazancas@mandriva.org> 0.5.0-2mdv2011.0
+ Revision: 626796
- add devel package and suggest of obconf plugin

* Thu Oct 14 2010 Funda Wang <fwang@mandriva.org> 0.5.0-1mdv2011.0
+ Revision: 585633
- New version 0.5.0

* Thu Jun 10 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.4.0-2mdv2010.1
+ Revision: 547856
- make lxappearance.desktop appear only in LXDE

* Thu Jan 07 2010 Funda Wang <fwang@mandriva.org> 0.4.0-1mdv2010.1
+ Revision: 487023
- New version 0.4.0

* Wed Dec 09 2009 Funda Wang <fwang@mandriva.org> 0.3.0-1mdv2010.1
+ Revision: 475335
- BR intltool
- new version 0.3.0

* Mon Jul 06 2009 Funda Wang <fwang@mandriva.org> 0.2.1-1mdv2010.0
+ Revision: 392807
- new version 0.2.1

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.2-2mdv2009.0
+ Revision: 268122
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 0.2-1mdv2009.0
+ Revision: 200930
- BR desktop-file-utils
- fix url
- import source
- Created package structure for lxappearance.

