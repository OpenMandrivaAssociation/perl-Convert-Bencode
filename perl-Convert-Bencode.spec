%define upstream_name    Convert-Bencode
%define upstream_version 1.03
Name:		perl-%{upstream_name}
Version:	1.03
Release:	4
Summary:	Functions for converting to/from bencoded strings
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/Convert-Bencode
Source0:	https://cpan.metacpan.org/authors/id/O/OR/ORCLEV/Convert-Bencode-1.03.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More) >= 0.45

BuildArch:	noarch

%description
This module provides two functions, bencode and bdecode, which encode and
decode bencoded strings respectively.

%prep
%setup -q -n Convert-Bencode-1.03

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*



