%define	lib_major	0

%define	lib_name		%mklibname %{name} %{lib_major}
%define	lib_name_devel		%mklibname %{name} -d
%define	lib_name_static_devel	%mklibname %{name} -s -d

Name:		glpk
Version:	4.47
Release:	%mkrel 1
Summary:	GLPK glpsol utility
License:	GPLv3+
Group:		Sciences/Mathematics
URL:		http://www.gnu.org/software/glpk/glpk.html
Source0:	http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	gmp-devel
BuildRequires:	tetex-latex
BuildRequires:	texinfo

%description
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the utility glpsol.

%package -n %{lib_name}
Summary:	GLPK shared libraries
Group:		Sciences/Mathematics
Obsoletes:	%{name} < %{version}

%description -n %{lib_name}
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the library needed to run programs dynamically
linked with GLPK.

%package -n %{lib_name_devel}
Summary:	Header files for development with GLPK
Group:		Development/C
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the headers needed to develop applications using
GLPK.

%package -n %{lib_name_static_devel}
Summary:	GLPK static libraries
Group:		Development/C
Requires:	%{lib_name_devel} = %{version}-%{release}

%description -n %{lib_name_static_devel}
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the static libraries necessary for developing
programs which use GLPK.

%prep
%setup -q

%build
%configure2_5x
%make

# Trust Knuth to produce a single-pass compiler for a multiple-pass language.
pushd doc
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex && \
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex && \
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex
texi2pdf -p gmpl.texi && \
popd

%install
%__rm -rf %{buildroot}

%makeinstall_std
# Clean out the examples directory so we can include it wholesale in %doc.
%make -C examples distclean
%__rm -rf examples/Makefile*

%clean
%__rm -rf %{buildroot}

%files
%attr(0755,root,root) %{_bindir}/glpsol

%files -n %{lib_name}
%{_libdir}/*.so.%{lib_major}*

%files -n %{lib_name_devel}
%doc examples doc/*.txt doc/*.pdf AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_includedir}/*.h
%{_libdir}/*.so

%files -n %{lib_name_static_devel}
%{_libdir}/*.a

