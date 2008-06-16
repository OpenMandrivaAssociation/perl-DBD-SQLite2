%define module	DBD-SQLite2
%define name	perl-%{module}
%define version	0.33
%define release	%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Summary:	Self Contained RDBMS in a DBI Driver (sqlite 2.x)
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/%{module}-%{version}.tar.bz2
Patch0:		perl-DBD-SQLite2-0.33-libsqlite0.patch
BuildRequires:	perl-devel
BuildRequires:	perl-DBI >= 1.03-1mdk
BuildRequires:	sqlite-devel
Buildroot:	%{_tmppath}/%{name}-%{version}

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

%setup -q -n %{module}-%{version}
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
%patch -p1 -E

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make CCFLAGS="$RPM_OPT_FLAGS" OPTIMIZE="-DNDEBUG=1 -DSQLITE_PTR_SZ=4"

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README* Changes
%{perl_vendorlib}/*
%{_mandir}/*/*


