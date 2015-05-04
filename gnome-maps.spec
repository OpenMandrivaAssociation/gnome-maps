%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-maps
Version:	3.14.2
Release:	%mkrel 1
Summary:	A map application for GNOME
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0) >= 2.39.3
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gjs-1.0) >= 1.39.0
BuildRequires:	gjs
Requires:	gjs
Requires:	geoclue >= 1.99.3

%description
%{name} is a map application for GNOME.

%prep
%setup -q
%apply_patches

%build
%configure2_5x --disable-schemas-compile
%make

%install
%makeinstall_std

# fix .desktop file
desktop-file-edit %{buildroot}%{_datadir}/applications/org.gnome.Maps.desktop

# we don't want these
find %{buildroot} -name "*.la" -delete

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc NEWS README
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/*
%{_datadir}/appdata/org.gnome.Maps.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Maps.service
%{_iconsdir}/*/*/apps/%{name}.*


%changelog
* Tue Nov 11 2014 ovitters <ovitters> 3.14.2-1.mga5
+ Revision: 796315
- new version 3.14.2

* Wed Oct 15 2014 umeabot <umeabot> 3.14.1.2-2.mga5
+ Revision: 749320
- Second Mageia 5 Mass Rebuild

* Mon Oct 13 2014 ovitters <ovitters> 3.14.1.2-1.mga5
+ Revision: 738320
- new version 3.14.1.2

* Sat Oct 11 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 738005
- new version 3.14.1

* Sun Sep 28 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 731354
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 679734
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 677579
- new version 3.13.92

* Wed Sep 03 2014 ovitters <ovitters> 3.13.91-1.mga5
+ Revision: 671185
- new version 3.13.91

* Sat Aug 09 2014 pterjan <pterjan> 3.13.4-2.mga5
+ Revision: 661216
- Try to fix parallel build

* Mon Jul 21 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655187
- new version 3.13.4

* Wed Jun 25 2014 ovitters <ovitters> 3.13.3-1.mga5
+ Revision: 639520
- new version 3.13.3

  + fwang <fwang>
    - drop unused switch

* Wed May 28 2014 fwang <fwang> 3.13.2-1.mga5
+ Revision: 627128
- update file list
- update file list

  + ovitters <ovitters>
    - new version 3.13.2

* Tue May 13 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622426
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614200
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 608018
- new version 3.12.0

* Mon Mar 17 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604500
- new version 3.11.92

* Tue Mar 04 2014 ovitters <ovitters> 3.11.91-1.mga5
+ Revision: 599482
- new version 3.11.91

* Tue Feb 18 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 594278
- new version 3.11.90

* Thu Feb 06 2014 dams <dams> 3.11.5.1-1.mga5
+ Revision: 584130
- new version 3.11.5.1

  + ovitters <ovitters>
    - new version 3.10.2

* Sat Oct 19 2013 umeabot <umeabot> 3.10.0-2.mga4
+ Revision: 536497
- Mageia 4 Mass Rebuild

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 484390
- new version 3.10.0

* Tue Sep 17 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480843
- new version 3.9.92

* Tue Sep 03 2013 wally <wally> 3.9.91-1.mga4
+ Revision: 474832
- require gjs and geoclue

  + ovitters <ovitters>
    - new version 3.9.91

* Fri Aug 23 2013 ovitters <ovitters> 3.9.90.2-1.mga4
+ Revision: 470341
- new version 3.9.90.2

* Wed Aug 21 2013 fwang <fwang> 3.9.90.1-1.mga4
+ Revision: 468658
- update file list

  + ovitters <ovitters>
    - new version 3.9.90.1

* Wed Jul 31 2013 ovitters <ovitters> 3.9.5-2.mga4
+ Revision: 461679
- fix description

* Wed Jul 31 2013 ovitters <ovitters> 3.9.5-1.mga4
+ Revision: 461671
- imported package gnome-maps

