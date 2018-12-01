%define upstream_name    Sereal-Encoder
%define upstream_version 4.005

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Fast, compact, powerful binary serialization
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    https://cpan.metacpan.org/authors/id/Y/YV/YVES/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data::Dumper)
BuildRequires: perl(ExtUtils::MakeMaker) >= 7.0.0
BuildRequires: perl(ExtUtils::ParseXS) >= 2.210.0
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sereal::Decoder) >= 3.0.0
BuildRequires: perl(Test::LongString)
BuildRequires: perl(Test::More) >= 0.880.0
BuildRequires: perl(Test::Warn)
BuildRequires: perl(XSLoader)
BuildRequires: perl-devel

%description
Devel::CheckLib is a perl module that checks whether a particular C library
and its headers are available.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
# (daviddavid) // build is broken:
%__make

%check
%__make test

%install
%make_install

%files
%doc Changes INSTALL META.json META.yml MYMETA.yml
%{_mandir}/man3/*
%{perl_vendorarch}/*
