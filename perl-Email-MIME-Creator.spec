#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	MIME-Creator
Summary:	Email::MIME::Creator - Email::MIME constructor for starting a new part
Summary(pl):	Email::MIME::Creator - konstruktor dla Email::MIME do rozpocz�cia nowej cz�ci
Name:		perl-Email-MIME-Creator
Version:	1.41
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94778bbd3637dd88e84632f015f07cdb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-MIME >= 1.7
BuildRequires:	perl-Email-MIME-Modifier >= 1.2
BuildRequires:	perl-Email-Simple >= 1.9
BuildRequires:	perl-Email-Simple-Creator >= 1.4
BuildRequires:	perl-Email-Date
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email::MIME::Creator is an Email::MIME constructor for starting a new
MIME part.

%description -l pl
Modu� Email::MIME::Creator stanowi konstruktor dla Email::MIME do
rozpocz�cia nowej cz�ci MIME wiadomo�ci e-mail.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Email/MIME/*.pm
%{_mandir}/man3/*