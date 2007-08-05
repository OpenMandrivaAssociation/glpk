%define	name	glpk
%define	version	4.20
%define	release %mkrel 1

%define lib_name_orig libglpk
%define lib_major 0
%define lib_name              %mklibname glpk %{lib_major}
%define lib_name_devel        %mklibname glpk %{lib_major} -d
%define lib_name_static_devel %mklibname glpk %{lib_major} -s -d

Summary:	GNU Linear Programming Kit
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sciences/Mathematics
URL:		http://www.gnu.org/software/glpk/glpk.html
Source0:	%{name}-%{version}.tar.bz2
#Patch1:		glpk-4.7_shared_lib.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

%package -n %{lib_name}
Summary:	Shared library and utility for LP and MIP
Group:		Sciences/Mathematics
Obsoletes:	%{name}
Provides: %{lib_name_orig} = %{version}-%{release} %{name} = %{version}-%{release}

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with GLPK and the utilitity glpsol.

%package -n %{lib_name_devel}
Summary:	Header files for development with GLPK
Group:		Development/C
Requires:	%{lib_name} = %{version}
Obsoletes:	%{name}-devel
Provides: %{lib_name_orig}-devel = %{version}-%{release} %{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
This package contains the headers needed to develop applications using
GLPK.

%package -n %{lib_name_static_devel}
Summary: Static libraries for GLPK
Group: Development/C
Requires: %{lib_name_devel} = %{version}

%description -n %{lib_name_static_devel}
This package contains the static libraries necessary for developing
programs which use GLPK. Install this package if you need to statically
link your program or library.

%prep

%setup -q
#%patch1 -p1

%build

# Trust Knuth to produce a single-pass compiler for a multiple-pass language.
cd doc
pdflatex -interaction=nonstopmode -file-line-error-style lang.latex && \
pdflatex -interaction=nonstopmode -file-line-error-style lang.latex && \
pdflatex -interaction=nonstopmode -file-line-error-style lang.latex
pdflatex -interaction=nonstopmode -file-line-error-style refman.latex && \
pdflatex -interaction=nonstopmode -file-line-error-style refman.latex && \
pdflatex -interaction=nonstopmode -file-line-error-style refman.latex
cd ..

%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
# Clean out the examples directory so we can include it wholesale in %doc.
make -C examples distclean
rm -rf examples/Makefile*

%clean
rm -rf %{buildroot}

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so.*
%attr(0755,root,root) %{_bindir}/glpsol

%files -n %{lib_name_static_devel}
%defattr(-, root, root)
%{_libdir}/*.a

%files -n %{lib_name_devel}
%defattr(-, root, root)
%doc examples doc/bench.txt AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_includedir}/*.h
%{_libdir}/*.la
%{_libdir}/*.so


