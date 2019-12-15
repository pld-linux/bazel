# TODO: use system jars
Summary:	Build and test software of any size, quickly and reliably
Summary(pl.UTF-8):	Budowanie i testowanie oprogramowania dowolnych rozmiarów - szybko i wiarygodnie
Name:		bazel
Version:	1.2.1
Release:	1
License:	Apache v2.0
Group:		Development/Tools
#Source0Download: https://github.com/bazelbuild/bazel/releases
Source0:	https://github.com/bazelbuild/bazel/releases/download/%{version}/%{name}-%{version}-dist.zip
# Source0-md5:	da63b5df0eb5075d6ed3e021ae79cf6b
Patch0:		%{name}-glibc.patch
Patch1:		%{name}-x86.patch
URL:		https://bazel.build/
BuildRequires:	bash
BuildRequires:	jdk >= 1.8
BuildRequires:	libstdc++-devel
BuildRequires:	python3 >= 1:3.2
BuildRequires:	unzip
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautostrip		.*%{_bindir}/bazel

%description
Build and test software of any size, quickly and reliably.

%description -l pl.UTF-8
Budowanie i testowanie oprogramowania dowolnych rozmiarów - szybko i
wiarygodnie.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%{__sed} -i -e 's,/bin/java" ,& -Xmx2g ,' scripts/bootstrap/compile.sh

%build
BAZEL_JAVAC_OPTS="-J-Xmx1g" \
EXTRA_BAZEL_ARGS="--host_javabase=@local_jdk//:jdk" \
bash ./compile.sh

%install
rm -rf $RPM_BUILD_ROOT

install -D output/bazel $RPM_BUILD_ROOT%{_bindir}/bazel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.md CONTRIBUTORS README.md
%attr(755,root,root) %{_bindir}/bazel
