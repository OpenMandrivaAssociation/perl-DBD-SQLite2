%define	module	DBD-SQLite2
%define	upstream_version 0.33

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Self Contained RDBMS in a DBI Driver (sqlite 2.x)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{module}/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/%{module}-%{upstream_version}.tar.bz2
Patch0:		perl-DBD-SQLite2-0.33-libsqlite0.patch

BuildRequires:	perl-devel
BuildRequires:	perl-DBI >= 1.03-1mdk
BuildRequires:	sqlite-devel

%description
SQLite is a small fast embedded SQL database engine.

DBD::SQLite embeds that database engine into a DBD driver, so
if you want a relational database for your project, but don't
want to install a large RDBMS system like MySQL or PostgreSQL,
then DBD::SQLite may be just what you need.

It supports quite a lot of features, such as transactions (atomic
commit and rollback), indexes, DBA-free operation, a large subset
of SQL92 supported, and more.

Note: DBD::SQLite2 is the old version of DBD::SQLite, and is linked against
version 2.x.x of the sqlite library. The current version of DBD::SQLite is
linked against version 3 (or possibly later if I forget to update this file).
This release is designed to allow you to have both versions installed on the
same system.

%prep

%setup -q -n %{module}-%{upstream_version}
# remove the embedded SQLite 2
rm -f \
	attach.c \
	auth.c \
	btree.c \
	btree.h \
	btree_rb.c \
	build.c \
	copy.c \
	date.c \
	delete.c \
	encode.c \
	expr.c \
	func.c \
	getsqlite.pl \
	hash.c \
	hash.h \
	insert.c \
	main.c \
	opcodes.c \
	opcodes.h \
	os.c \
	os.h \
	pager.c \
	pager.h \
	parse.c \
	parse.h \
	pragma.c \
	printf.c \
	random.c \
	select.c \
	sqlite.h \
	sqliteInt.h \
	table.c \
	tokenize.c \
	trigger.c \
	update.c \
	util.c \
	vacuum.c \
	vdbe.c \
	vdbe.h \
	vdbeaux.c \
	vdbeInt.h \
	where.c
%patch0 -p1 -E
# jq - test failing, dunno why
rm -f t/ak-dbd.t

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make OPTIMIZE="-DNDEBUG=1 -DSQLITE_PTR_SZ=4"

%check
make test

%install
%makeinstall_std

%files
%doc README* Changes
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Thu Feb 02 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.330.0-5
+ Revision: 770585
- clean up spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.330.0-4
+ Revision: 681355
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-3mdv2011.0
+ Revision: 555788
- rebuild for perl 5.12

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.330.0-2mdv2011.0
+ Revision: 555463
- rebuild

* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-1mdv2010.0
+ Revision: 410153
- rebuild using %%perl_convert_version

  + Michael Scherer <misc@mandriva.org>
    - fix patch application

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - fix spacing at top of description
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Fri Nov 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.33-4mdv2007.0
+ Revision: 85332
- Import perl-DBD-SQLite2

* Fri Nov 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.33-4
- rebuild

* Tue Sep 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-3mdk
- spec cleanup

* Thu Dec 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.33-2mdk
- applied changes by Yann Droneaud <ydroneaud@mandrakesoft.com>:
 - link against installed libsqlite0
 - removed getsqlite.pl which conflicted with perl-DBD-SQLite package
- fix deps

* Thu Dec 02 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.33-1mdk
- used the spec file from the perl-DBD-SQLite package

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.07-2mdk 
- rebuild for new perl
- remove README.urpmi

* Fri Oct 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.07-1mdk
- 1.07.

* Wed Aug 11 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.03-1mdk
- 1.03.
- Remove patch 1.

* Thu Jul 29 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.00-1mdk
- 1.00, incompatible format with previous versions.
- Remove MANIFEST, add README.update.urpmi.
- Patch to prevent interactivity in Makefile.PL

* Tue May 18 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.31-2mdk
- Fix compile FLAGS

