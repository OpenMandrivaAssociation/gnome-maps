%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define __noautoreqfiles org.gnome.Maps$

Name:		gnome-maps
Version:	40.0
Release:	2
Summary:	A map application for GNOME
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Source100:	gnome-maps.rpmlintrc
BuildRequires:  appstream-util
BuildRequires:	intltool
BuildRequires:	pkgconfig(champlain-0.12)
BuildRequires:	pkgconfig(folks)
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0) >= 2.39.3
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gjs-1.0) >= 1.39.0
BuildRequires:	pkgconfig(geocode-glib-1.0)
BuildRequires:	pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:	gjs
BuildRequires:  meson
Requires:	gjs
Requires:	geoclue >= 1.99.3
#Requires: typelib(GjsPrivate)
Requires: typelib(GFBGraph)
Requires: typelib(GtkChamplain)
Requires: typelib(GtkClutter)
Requires: typelib(WebKit2)
Requires: typelib(Handy)

%description
%{name} is a map application for GNOME.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

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
%{_datadir}/metainfo/org.gnome.Maps.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Maps.service
%{_iconsdir}/*/*/apps/org.gnome.Maps*.*
%{_libdir}/%{name}
#{_datadir}/gir-1.0/GnomeMaps-1.0.gir
