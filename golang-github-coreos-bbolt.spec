# https://github.com/coreos/bbolt
%global goipath         github.com/coreos/bbolt
%global commit          32c383e75ce054674c53b5a07e55de85332aee14

%gometa -i

Name:           %{goname}
Version:        1.3.1
Release:        0.3.coreos.5%{?dist}
Summary:        An embedded key/value database for Go
# Detected licences
# - MIT/X11 (BSD like) at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
# Consumes too much memory
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.3.1-0.2.coreos.5.20180309git32c383e
- Upload glide files

* Fri Mar 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.3.1-0.1.coreos.5.20180309git32c383e
- First package for Fedora
  resolves: #1553730
