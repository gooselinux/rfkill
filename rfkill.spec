Name:           rfkill
Version:        0.3
Release:        4%{?dist}
Summary:        A tool for enabling and disabling wireless devices

Group:          System Environment/Base
License:        ISC
URL:            http://www.linuxwireless.org/en/users/Documentation/rfkill
Source0:        http://wireless.kernel.org/download/rfkill/rfkill-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch0:         rfkill-default-install-to-PREFIX-sbin.patch

%description
rfkill is a simple tool for accessing the Linux rfkill device interface,
which is used to enable and disable wireless networking devices, typically
WLAN, Bluetooth and mobile broadband.

%prep
%setup -q
%patch0 -p 1


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=${RPM_BUILD_ROOT} PREFIX='' MANDIR=%{_mandir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/sbin/rfkill
%{_mandir}/man1/*
%doc COPYING README


%changelog
* Mon Feb 25 2010 John W. Linville <linville@redhat.com> 0.3-4
- Correct license tag from BSD to ISC
- Use correct email address in changelog entries -- oops..

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.3-3.1
- Rebuilt for RHEL 6

* Tue Sep 29 2009 John W. Linville <linville@redhat.com> 0.3-3
- Install binary into /sbin to enable use during boot

* Tue Sep 15 2009 John W. Linville <linville@redhat.com> 0.3-2
- Change summary and description as suggested by Tomasz Torcz <zdzichu@irc.pl>

* Thu Sep  3 2009 John W. Linville <linville@redhat.com> 0.3-1
- Update to upstream version 0.3
- Use 'make install' and include man page in files section

* Tue Aug 25 2009 John W. Linville <linville@redhat.com> 0.1-1
- Initial import
